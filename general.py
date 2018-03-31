import os
def create_prjct(directory):
    if not os.path.exists(directory):
        print("creating project" + directory)
        os.makedirs(directory)
create_prjct('pinka')

def create_file(project,base_url):
    queue=project+'/queue.txt'
    crawled=project+'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()


# create_file('pinka','https://www.techgig.com/')

def append_file(path,data):
    with open(path,'a') as file:
        file.write(data+"\n")


def del_file(path):
    with open(path,'w'):
        pass


#read a file and convert each line to set item
def file_set(filename):
    results=set()
    with open(filename,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#set to a file

def set_file(links,file):
    del_file(file)
    for link in sorted(links):
        append_file(file,link)

