
def si_o_no_entero(chain: str):
   chain = chain.strip()
   return chain.isdigit() or (chain.startswith("-") and chain[1:].isdigit())
   
def num_entero():
    chain = input("Meta un número entero: ")

    while not si_o_no_entero(chain):
        chain = input("**ERROR** Eso no es un entero majaron\n\nMeta un número entero: ")

    return int(chain)

def main():
    num = num_entero()
    print(f"Has metido el número {num}")


if __name__ == "__main__": 
    main()