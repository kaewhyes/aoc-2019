#!/usr/bin/env luajit

local file = io.open("input.txt", "r") -- opens input as a read only file

local total = 0 -- init total as 0
for line in file:lines() do -- 
    total = total + math.floor(line / 3) - 2 -- no += :( (also finding the fuel)
end
print(total) -- give us the solution
