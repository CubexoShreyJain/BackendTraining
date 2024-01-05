def seqPrinter(n = 10):
    try:
        for i in range(n+1):
            print(i*i)
            print()
    except Exception as e:
        print("Error occured: ", e)

seqPrinter()

