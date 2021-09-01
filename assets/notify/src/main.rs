use notify_rust::Notification;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    Notification::new()
        .summary(&args[1])
        .body(&args[2])
        .appname("Bannoti")
        .timeout(3)
        .show()
        .expect("Ugh");
}
