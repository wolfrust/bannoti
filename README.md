```

                     ____                          _   _
                     | __ )  __ _ _ __  _ __   ___ | |_(_)
                     |  _ \ / _` | '_ \| '_ \ / _ \| __| |
                     | |_) | (_| | | | | | | | (_) | |_| |
                     |____/ \__,_|_| |_|_| |_|\___/ \__|_|

                                        Desktop notifier for banano (https://banano.cc)
                                         by Mateo Cruz  (https://github.com/wolfrust)


```


✨You can use Bannoti to recieve notifications for Banano transactions on your computer. 


---


**For everything below, replace `bannoti.py` with the file in your tree. (`bannoti.exe` on windows and `bannoti` on Linux)**


### Installation

Using already compiled excuctables is the recommended option, as you will simply have to run the excecutable without installing any programming languages. 
However, if you'd like to use the source code, that is documented as well below.

#### Compiled 


1. Grab [the latest release](https://github.com/wolfrust/bannoti/releases/latest).
2. Unzip the file you just downloaded
3. Open a terminal window
4. [Move into the directory](https://help.ubuntu.com/community/UsingTheTerminal) in which you placed the files
5. Run ```bannoti.py --startup``` to add Bannoti to startup

Step 5 is optional but recommended, because otherwise you will have to start Bannoti manually *every time you log on*, which could get annoying.


#### Source

Installing through source is a bit more gritty, but not very hard. 

1. Install [Rust](https://rust-lang.org) and [Python (3)](https://python.org). 
2. Download Bannoti's [source code](https://github.com/wolfrust/bannoti/releases/latest). 
3. Unzip the file you just downloaded.
4. Open a terminal window.
5. Move into the directory of the files.
6. Move into assets/notify/
7. Run `cargo build`. This will build the binary.
8. Run `mv target/debug/notify ..` (Linux) or `move target\debug\notify.exe ..` (Windows) 
9. Move back into the root of the project : `cd ../../`
10. Delete the assets/notify/ directory : `rm -rf assets/notify/`. **Make sure you type this out carefully, because you don't want to end up deleting the binary we just made.**

At this point you can do two things.
1. Start using Bannoti without compiling bannoti.py : Run `python bannoti.py --startup`, and you're ready.
2. Compile bannoti.py as well. Please refer to [this guide](https://datatofish.com/executable-pyinstaller/) if you do not know how to compile python files.

---

### Usage (20s) ⌨

Running ``` bannoti.py --help ``` will show you a nice help message.

```

$> bannoti.py --help


  -- snip --


    bannoti.py <option>

    run : run the program
    --add : add an address to get notified for
    --remove : stop getting notifications for an address
    --gettracked : get tracked accounts
    --startup : add program to startup

    If this is your first time using Bannoti, I recommend you see the README (./README.md).


```

It's pretty straightforward. You don't have to supply any other arguments, just one of these.

For example : `bannoti.py --add`


---

#### Contribution (4s)

All contributions are welcome.


#### Feature Requests & Bug Reporting (4s) 🐞

GitHub provides the [issues tab](https://github.com/wolfrust/bannoti/issues) for this. 

---

#### Contact 📱

You can contact me using one of the means listed in my [profile](https://github.com/wolfrust/wolfrust/README.md#reach-me).

---

#### Tips 😘

I'd really appreciate it. Every bit of potassium matters.

Banano : ban_3qhzq3kxhe95hdq3q6uzmqg7ewp5js8ebcoxq1httmguzf7s5bb3a9894waf
Nano : nano_1rhj7y5hkm5sx5rcn3p5tgsgyij1qwty1ja66197yacw3sjwoob3yyc76jbt

If you'd like to tip me via some other means, please [contact me](https://github.com/wolfrust/wolfrust/#reach-me).
