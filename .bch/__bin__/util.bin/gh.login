#!/usr/bin/env bash

gh auth login --with-token < ${HOME}/.ssh/github.d/github.token.bryan-forever
gh auth status
