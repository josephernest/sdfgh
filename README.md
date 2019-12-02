# sdfgh

## Why this name?

"sdfgh" are consecutive letters from the second row of a QWERTY or AZERTY keyboard, the kind of letters you type when you need a random name.

## What's the goal?

We often hear:

> Don't trust an encryption program if it's not open-source

This is true, and here it's even:

*"Don't trust an encryption program if you cannot read its source code completely in 10 minutes."*

You want to use it this program for your personal notes? Just take 10 minutes to read the 65 lines of code(*).

## Why another lightweight notepad with encryption?

I needed an encrypted notepad for personal notes that has these features:

* Ask a password on startup
* Don't re-ask for the password when saving since we already asked that when opening (except if it's a new file)
* Open-source
* Dark mode colors
* The unencrypted plaintext is **never** written to disk
* I wanted to be able to read the full source-code before using it, without spending 1 full day on it

(*) Ok, you still have to trust Python code (I think it's ok) and [PyCryptoDome](https://pypi.org/project/pycryptodome/).

## How to use it?

Just run `python sdfgh.py`. That's all.

## License

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Contributions

Feel free to post issues.
NB: This project will (probably) never be made longer than 100 lines of code, so nearly no new features will be added. (No modular splitting into several .py files will be done, and no re-structuring with `Class MyEditor:` as well, etc.)

## Author

[@JosephErnest](https://twitter.com/josephernest) on Twitter

More on https://afewthingz.com.
