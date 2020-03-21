clc,clear;
% input the caseName, the caseName you can see the MATPOWER-manual.pdf in details(if you have installed Matpower)
str_caseName = '...input the caseName...';
% input your path where you want creat the case file
filePath = 'X:\...\...\...'
caseName = eval(str_caseName);
bus = caseName.bus;
gen = caseName.gen;
brch = caseName.branch;
gencost = caseName.gencost;

file = [filePath, str_caseName];
if ~exist(file, 'dir')
    mkdir(file);
end

%addpath(file);
dlmwrite([file, '\bus.dat'] , bus);
dlmwrite([file, '\gen.dat'] , gen);
dlmwrite([file, '\gencost.dat'] , gencost);
dlmwrite([file, '\brch.dat'] , brch);
