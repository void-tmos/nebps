run("cp /tmp/nebps/nebps-install.py /py/nebps-install.py")
run("mkdir -p /etc/nebps")
if not os.path.exists(file("/etc/nebps/installed.conf")):
    run("cp /tmp/nebps/installed.conf /etc/nebps/installed.conf")
if not os.path.exists(file("/etc/nebps/repo.list")):
    run("cp /tmp/nebps/repo.list /etc/nebps/repo.list")
run("mkdir -p /etc/nebps/repos")
