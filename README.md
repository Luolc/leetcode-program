# LeetCode Program

[![Build Status](https://travis-ci.org/Luolc/leetcode-program.svg?branch=master)](https://travis-ci.org/Luolc/leetcode-program)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
![PullRequest](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

I created this as a productive tool for practicing LeetCode online judge. It is mainly for Google's interview
in the near future. It aims to use the powerful utilities of Travis-CI and GitHub to do the boring things: choosing
which questions to solve, creating issue for today's task...

## My Solutions

Feel free to check my solutions of LeetCode questions on [http://www.luolc.com/leetcode-program/](http://www.luolc.com/leetcode-program/). :D

## Setup

### Fork and Clone

Just fork and clone this repository.

### Project Configure

To appease your custom needs, there are several constants in `core/constant.py` that could be set.

- `USERNAME`: You **HAVE TO** change this to your GitHub account, otherwise the GitHub related service would fail.
- `CRON_CONFIG`: You could set how many tasks to create each day.

The solutions should be placed in `res/solutions/`. Each question has a directory named as its number.
You could delete all the solutions I created and start writing yours.

### Travis-CI Settings

- Turn on this repository on your Travis-CI.
- Add an environment variable `GITHUB_TOKEN` with the value of your [GitHub OAuth token](https://github.com/settings/tokens).
- Turn on daily cron jobs for this repository.

## Usage

There are some useful utilities that save you from the boring tasks.

### Fetch LeetCode Algorithm Problems

Running the following command, then a `leetcode-questions.json` would be generated in the `res` folder.

```bash
$ python3 core/core.py update_local_questions --js_path=/usr/local/bin/phantomjs
```

> `js_path` represents the path to [PhantomJS](http://phantomjs.org/). You have to prepare it in advance.
>
> If you are MacOS user, just simply use `$ brew install phantonjs` to download it.

### Create random daily tasks

This would create random tasks as issues in this repository. The number of tasks could be set in `core/constant.py`.

```bash
$ python3 core/core.py create_daily_task --token=$GITHUB_TOKEN
```

Travis-CI has cron jobs running the command every day. But you could still run it manually to create issues,
in case you want some more questions to practice some day. :D

### Generate solution pages

This would help you generate the solution pages from the source in `res/solutions` folder.
The generated solutions would be in `build` folder. 

```bash
$ python3 core/core.py generate_solutions
```

With the help of Travis-CI, the solutions would be deployed to [GitHub Pages of this repository](http://www.luolc.com/leetcode-program/).

## To-Do List

- [x] LeetCode problems spider
- [x] Automatic issue creator powered by Travis-CI
- [x] Solution page generation and deployment
- [ ] Testing the solutions' format.

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
