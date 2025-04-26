Yes, by default, Django signals run in the same thread as the caller. Django’s signal handling is synchronous by default, meaning that when a signal is sent, the connected receiver function is executed immediately in the same thread and the same process as the sender.

In this django app When a new Post is created, the signal handler will be triggered, and it should print the thread information to the console.

Like this : "Post saved! Title: Test Post
Is this happening in a new thread? <_MainThread(MainThread, started 12345)>
"

This proves that the signal is executed in the same thread as the sender (which is the main thread).

By default, Django signals are synchronous. This means when a signal is triggered, the connected receiver function is executed
in the same thread and the same process as the action (such as saving a model). You can confirm this by checking the thread 
info (threading.current_thread()), which shows that the signal handler runs in the same thread.
