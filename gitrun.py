import subprocess

while True:
    p = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    print(out.decode("utf-8").split("\n"))
    print("=====")


    p = subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE)
    out, err = p.communicate()
    print(out.decode("utf-8").split("\n"))
    print("=====")

    p = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    outlist = out.decode("utf-8").split("\n")
    print(outlist)

    finalfilelist = []
    for elem in outlist:
        if "\tnew file:" in elem:
            finalfilelist.append(elem)

    print(finalfilelist)

    finalfolderlist = []
    for elem in finalfilelist:
        try:
            finalfolderlist.append(elem.replace("\tnew file:", "").strip().split("/")[0])
        except Exception as e:
            pass

    print(finalfolderlist)
    freq = {x: finalfolderlist.count(x) for x in finalfolderlist}
    print(freq)
    max_key = max(freq, key=freq.get)

    print(max_key)
    print("=====")

    p = subprocess.Popen(["git", "commit", "-m", max_key], stdout=subprocess.PIPE)
    out, err = p.communicate()
    print(out.decode("utf-8").split("\n"))
    print("=====")
