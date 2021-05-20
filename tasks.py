from invoke import task 

@task
def build(c, docs=False):
    c.run("docker build -t super-ros-node .")