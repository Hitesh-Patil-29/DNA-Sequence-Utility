dna = ""
while True:
    print("1 input and validation")
    print("2 DNA analysis")
    print("3 DNA operations")
    print("4 exit")

    choice = input("enter your choice: ")
    if choice == "1":
        while True:
            print("1 enter DNA sequence")
            print("2 check sequence validity")
            print("3 back to main menu")

            subchoice = input("enter your choice: ")

            if subchoice == "1":
                dna = input("input DNA sequence = ").upper()
                print("sequence recorded")

            elif subchoice == "2":
                if dna == "":
                    print("input DNA sequence first.")
                else:
                    valid = True

                    for base in dna:
                        if base not in "ATGC":
                            valid = False
                            break

                    if valid:
                        print("valid DNA sequence.")
                    else:
                        print("invalid DNA sequence.")

            elif subchoice == "3":
                break

            else:
                print("wrong choice")
# dna analysis
    elif choice == "2":
        while True:
            print("1 perform basic analysis")
            print("2 compare two sequences")
            print("3 back to main menu")

            subchoice = input("enter your choice")

            if subchoice == "1":
                if dna == "":
                    print("input DNA sequence first.")
                else:
                    A = dna.count("A")
                    T = dna.count("T")
                    G = dna.count("G")
                    C = dna.count("C")

                    print("Length:", len(dna))
                    print("A:", A)
                    print("T:", T)
                    print("G:", G)
                    print("C:", C)

                    gc = ((G + C) / len(dna)) * 100
                    print("GC content =", gc, "%")

            elif subchoice == "2":
                if dna == "":
                    print("input first DNA sequence.")
                else:
                    dna2 = input("input second DNA sequence = ").upper()

                    if len(dna) != len(dna2):
                        print("Both DNA sequences have different lengths.")
                    else:
                        s = 0
                        for i in range(len(dna)):
                            if dna[i] == dna2[i]:
                                s += 1

                        match = (s / len(dna)) * 100
                        print("matching bases =", s)
                        print("DNA match =", round(match, 1), "%")

            elif subchoice == "3":
                break

            else:
                print("wrong choice")
# dna operations
    elif choice == "3":
        while True:
            print("1 find complement")
            print("2 find reverse complement")
            print("3 transcribe DNA")
            print("4 back to main menu")

            subchoice = input("enter your choice: ")

            if subchoice == "1":
                if dna == "":
                    print("input DNA sequence first.")
                else:
                    complement = ""

                    for base in dna:
                        if base == "A":
                            complement += "T"
                        elif base == "T":
                            complement += "A"
                        elif base == "G":
                            complement += "C"
                        elif base == "C":
                            complement += "G"

                    print("complement =", complement)

            elif subchoice == "2":
                if dna == "":
                    print("input DNA sequence first.")
                else:
                    complement = ""

                    for base in dna:
                        if base == "A":
                            complement += "T"
                        elif base == "T":
                            complement += "A"
                        elif base == "G":
                            complement += "C"
                        elif base == "C":
                            complement += "G"

                    print("reverse complement =", complement[::-1])

            elif subchoice == "3":
                if dna == "":
                    print("input DNA sequence first.")
                else:
                    rna = dna.replace("T", "U")
                    print("RNA sequence =", rna)

            elif subchoice == "4":
                break

            else:
                print("wrong choice")
# exit
    elif choice == "4":
        print("DNA analysis completed.")
        break

    else:
        print("wrong choice")