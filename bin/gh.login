#!/usr/bin/env bash
gh auth login --with-token < ${HOME}/.BRYAN.cred/gh.bryanhann.access.token
gh auth status
