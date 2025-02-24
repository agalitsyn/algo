package main

import (
	"context"
	"fmt"
	"log"
	"sync"
	"time"
)

type Task struct {
	ID int
}

func (t Task) Execute() {
	<-time.After(time.Second)
	log.Printf("execute task id=%d\n", t.ID)
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	taskExecutor := NewTaskExecutor(ctx, 5, 10)
	defer taskExecutor.Stop()

	for i := 0; i < 11; i++ {
		if err := taskExecutor.ScheduleTask(Task{ID: i + 1}); err != nil {
			log.Printf("ERR: %s", err)
			break
		}
	}
}

type TaskQueue struct {
	tasks chan Task
	wg    sync.WaitGroup
}

func NewTaskExecutor(ctx context.Context, workersLimit int, tasksLimit int) *TaskQueue {
	wp := &TaskQueue{
		tasks: make(chan Task, tasksLimit),
	}

	wp.wg.Add(workersLimit)
	for i := 0; i < workersLimit; i++ {
		go wp.worker(ctx)
	}

	return wp
}

func (te *TaskQueue) ScheduleTask(task Task) error {
	select {
	case te.tasks <- task:
		return nil
	default:
		return fmt.Errorf("could not schedule task with id=%d", task.ID)
	}
}

func (te *TaskQueue) Stop() {
	close(te.tasks)
	te.wg.Wait()
}

func (te *TaskQueue) worker(ctx context.Context) {
	defer te.wg.Done()

	for {
		select {
		case task, ok := <-te.tasks:
			if !ok {
				return
			}
			task.Execute()
		case <-ctx.Done():
			log.Println(ctx.Err())
			return
		}
	}
}
