#!/bin/bash

grep "ERROR" server.log | sed -E 's/.*\(IP:([0-9.]+)\).*Code:([0-9]+)/\1 - Hata:\2/'