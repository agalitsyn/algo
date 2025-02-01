package main

import (
	"context"
	"testing"
)

func TestTaskQueue(t *testing.T) {
	ctx := context.Background()
	q := NewTaskExecutor(ctx, 2, 3)
	defer q.Stop()

	// Test queue limit
	for i := 0; i < 5; i++ {
		err := q.ScheduleTask(Task{ID: i})
		if i < 3 && err != nil {
			t.Errorf("expected no error, got %v", err)
		}
		if i >= 3 && err == nil {
			t.Error("expected error, got nil")
		}
	}
}
