def Read(dir):
    require = []
    f = open(dir, encoding='gb18030', errors='ignore')
    line = f.readline()
    while line:
        line = line.strip().strip('\n')#去掉首尾的空格和换行符
        line = line.split('\t')#按照tab分割
        require.append(line[1].strip().split(' '))
        line = f.readline()
    return require
