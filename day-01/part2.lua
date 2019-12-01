#!/usr/bin/env luajit

function total_fuel(fuel) 
    
    --[[

    recursion!

    same thing as python tbh

    --]]

    local fuels_fuel = math.floor(fuel / 3) - 2
    if fuels_fuel <=0 then
        return 0
    else 
        return fuels_fuel + total_fuel(fuels_fuel)
    end
end

local file = io.open("input.txt", "r")

local total = 0
for line in file:lines() do
    total = total + total_fuel(line)
end
print(total)