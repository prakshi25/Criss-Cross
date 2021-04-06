l1=["_","_","_","_","_","_","_","_","_"]
t=0
while(t!=9):
    def array():
        print(l1[0],"|",l1[1],"|",l1[2])
        print(l1[3],"|",l1[4],"|",l1[5])
        print(l1[6],"|",l1[7],"|",l1[8])
        print("\n")
    array()
    n=int(input("Enter Your Position:"));

    if(t%2==0):
        l1[n-1]=1;
    else:
        l1[n-1]=0;
    
    if((l1[0]==1 and l1[1]==1 and  l1[2]==1) or (l1[3]==1 and  l1[4]==1 and  l1[5]==1) or (l1[6]==1 and  l1[7]==1 and  l1[8]==1) or (l1[0]==1 and  l1[3]==1 and  l1[6]==1) or (l1[1]==1 and  l1[4]==1 and  l1[7]==1) or (l1[2]==1 and  l1[5]==1 and  l1[8]==1) or (l1[0]==1 and  l1[4]==1 and  l1[8]==1) or (l1[2]==1 and  l1[4]==1 and  l1[6]==1)):
        print("\n1st Player Wins");
        break;

    elif((l1[0]==0 and l1[1]==0 and  l1[2]==0) or (l1[3]==0 and  l1[4]==0 and  l1[5]==0) or (l1[6]==0 and  l1[7]==0 and  l1[8]==0) or (l1[0]==0 and  l1[3]==0 and  l1[6]==0) or (l1[1]==0 and  l1[4]==0 and  l1[7]==0) or (l1[2]==0 and  l1[5]==0 and  l1[8]==0) or (l1[0]==0 and  l1[4]==0 and  l1[8]==0) or (l1[2]==0 and  l1[4]==0 and  l1[6]==0)):
        print("\n2nd Player Wins");
        break;
	
    if(t==9):
        print("\nDraw Match");
    t=t+1

