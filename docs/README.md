```

                     ____                          _   _
                     | __ )  __ _ _ __  _ __   ___ | |_(_)
                     |  _ \ / _` | '_ \| '_ \ / _ \| __| |
                     | |_) | (_| | | | | | | | (_) | |_| |
                     |____/ \__,_|_| |_|_| |_|\___/ \__|_|

                                        Desktop notification tool for banano (https://banano.cc)
                                         by @clocked07 (https://github.com/clocked07)


```


✨You can use Bannoti to receive notifications for Banano transactions on your computer.


---


**For everything below, replace `bannoti.py` with the file in your tree. (`bannoti.exe` on windows and `bannoti` on Linux)**


### Installation 🍕

Using already compiled executables is the recommended option, as you will simply have to run the executable without installing any programming languages.
However, if you'd like to use the source code, that is documented as well below.

#### Compiled (5m)


1. Grab [the latest release](https://github.com/clocked07/bannoti/releases/latest).
2. Unzip the file you just downloaded
3. Open a terminal window
4. [Move into the directory](https://help.ubuntu.com/community/UsingTheTerminal) in which you placed the files
5. Run ```bannoti.py --yesstartup``` to add Bannoti to startup

Step 5 is optional but recommended, because otherwise you will have to start Bannoti manually *every time you log on*, which could get annoying.


#### Source (15m)

Installing through source is a bit more gritty, but not very hard.

1. Install [Rust](https://rust-lang.org) and [Python (3)](https://python.org).
2. Download Bannoti's [source code](https://github.com/clocked07/bannoti/releases/latest).
3. Unzip the file you just downloaded.
4. Open a terminal window.
5. Move into the directory of the files.
6. Run `pip install -r config/requirements.txt` to install required python modules.
7. Move into assets/notify/
8. Run `cargo build --release`. This will build the binary.
9. Run `mv target/debug/notify ..` (Linux) or `move target\debug\notify.exe ..` (Windows)
10. Move back into the root of the project : `cd ../../`
11. Delete the assets/notify/ directory : `rm -rf assets/notify/`. **Make sure you type this out carefully, because you don't want to end up deleting the binary you just made.**

At this point you can do two things.
1. Start using Bannoti without compiling bannoti.py : Run `python bannoti.py --yesstartup`, and you're ready.
2. Compile bannoti.py as well. Please refer to [this guide](https://datatofish.com/executable-pyinstaller/) if you do not know how to compile python files.

---

### Usage ⌨

Running ``` bannoti.py --help ``` will show you a nice help message.

```

$> bannoti.py --help


  -- snip --


    bannoti.py <option>

    run : run the program
    --add : add an address to get notified for
    --remove : stop getting notifications for an address
    --gettracked : get tracked accounts
    --yesstartup : add program to startup (windows only)
    --nostartup : remove program from startup (windows only)


    If this is your first time using Bannoti, I recommend you see the README (docs/README.md).


```

It's pretty straightforward. You don't have to supply any other arguments, just one of these.

For example : `$> bannoti.py --add`


---

### Updating 🚀

It would be rather tedious to have to reconfigure settings every time a new version of Bannoti is released. 
Fortunately, all you have to do is copy over the `track.ini` file to the new assets/ directory.

For example, from `bannoti-v1.1/assets/track.ini` to `bannoti-v1.2/assets/track.ini`.

Bannoti follows [semantic versioning](https://semver.org/), meaning:

- v1.0.0 -> v1.0.1 : copy over track.ini
- v1.0 -> v1.1 : copy over track.ini
- v1 -> v2 : got to set it up from scratch


---

### Tips 😘

A small tip would go a long way :).

Banano 🍌 : `ban_1378hqogtx33j1inek3j97rng1qpr457iucmcetqmioqj1335cm8ea9iiunf`

Nano 🍂 : `nano_1rhj7y5hkm5sx5rcn3p5tgsgyij1qwty1ja66197yacw3sjwoob3yyc76jbt`

If you'd like to tip me via some other means, please [contact me](mailto:901aditya109@gmail.com).

---


### Safety 🐙

Bannoti is free of any malware and bloatware. I provide binary packages to make things easier for you, but if you'd rather install through the source code, that's documented as well. You can look at the source code yourself to verify that nothing's sus. So I think it's reasonable to conclude that **your computer is safe.**

**Bannoti cannot access your wallet**. It relies on public information to do it's thing. This means **your funds are safe.**

**Bannoti respects your privacy.** It doesn't ask for any confidential information, just addresses. They are stored offline in `assets/track.ini` on your computer.

Please note that some antivirus programs throw false positives on scanning Bannoti. This happens with all programs made using pyinstaller, which is a highly reputed compiler for python. If you take a look at [this virustotal scan](https://www.virustotal.com/gui/file/8611ee33bdae7a80493f992a5458495bf66f824cec209dc564a103af6ca5bd4b), you'll find that only 9/63 antivirus programs classify Bannoti as malware. If you head into the section on behaviour, you can see that the excecutable does nothing fishy.

---

### Legal ⚖

Bannoti is licensed under the BSD 3-Clause "New" or "Revised" License. You can find it [here](https://github.com/clocked07/bannoti/blob/main/docs/LICENSE). A short summary is given below.

![Bannoti's License](bsd-license-quick.png)



The tool that *sends the notifications* is called [notify-rust](https://github.com/hoodie/notify-rust), and is distributed under [this license](https://github.com/hoodie/notify-rust/blob/main/LICENSE-Apache).

The tool that allows python to interact with the Banano API is [bananopy](https://github.com/milkyklim/bananopy), and is distributed under [this license](https://github.com/milkyklim/bananopy/blob/master/LICENSE). It is Copyright (c) 2020 milkyklim.

---

### Feature Requests & Bug Reporting  🐞

Please use the [issues tab](https://github.com/clocked07/bannoti/issues) for this, as that provides me with an organized way to look at requests & reports.
For bug reports, please attach the `bug` label, and for feature requests please attach the `enhancment` label.

---

### Credits

This project would not have been possible without [bananopy](https://github.com/milkyklim/bananopy) by @milkyklim, and [notify-rust](https://github.com/hoodie/notify-rust) by @hoodie.

---


### Contact 📱

You can email me at 901aditya109@gmail.com.


---

![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fclocked07%2Fbannoti)
![GitHub Repo stars](https://img.shields.io/github/stars/clocked07/bannoti?style=social)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/clocked07/bannoti?label=latest%20release&color=blue)
![GitHub all releases](https://img.shields.io/github/downloads/clocked07/bannoti/total?color=9cf)

![Python version](https://img.shields.io/badge/python-3.9-blue)
![Development Status](https://img.shields.io/badge/development%20status-active-blueviolet)
![Versioning Type](https://img.shields.io/badge/versioning-semantic-ff69b4)

