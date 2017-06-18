# LeetCode Program

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
![PullRequest](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

I created this as a productive tool for practicing LeetCode online judge. It is mainly for Google's interview
in the near future. It aims to use the powerful utilities of Travis-CI and GitHub to do the boring things: choosing
which questions to solve, creating issue for today's task...

## Usage

There are some useful utilities to save you from the boring tasks.

### Fetch LeetCode Algorithm Problems

Running the following command, then a `leetcode-questions.json` would be generated in the `res` folder.

```bash
$ python3 core/core.py update_local_questions --js_path=/usr/local/bin/phantomjs
```

> `js_path` represents the path to [PhantomJS](http://phantomjs.org/). You have to prepare it in advance.
>
> If you are MacOS user, just simply use `$ brew install phantonjs` to download it.

## To-Do List

- [x] LeetCode problems spider
- [ ] Automatic issue creator powered by Travis-CI
- [ ] Solution page generation and deployment

## Author
- GitHub: [@Luolc](https://github.com/Luolc)

## License
```
  GNU GENERAL PUBLIC LICENSE
  Version 3, 29 June 2007

  Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
  Everyone is permitted to copy and distribute verbatim copies
  of this license document, but changing it is not allowed.
```
