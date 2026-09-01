def main():
    n=input()
    compressed=[]
    count=1
    for i in range(1,len(n)):
        if n[i]==n[i-1]:
            count+=1
        else:
            compressed.append(f'{n[i-1]}{count}')
            count=1
    compressed.append(f'{n[-1]}{count}')
    compressed_str=''.join(compressed)
    print(compressed_str if len(compressed_str)<len(n) else n)
main()    
