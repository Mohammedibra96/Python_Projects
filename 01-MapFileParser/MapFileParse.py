import re
import sys
def fun(string):
  f=open('Project_Memory_Map_File.map','r')
  text=f.read()
  Counter1=0
  Counter2=0
  Counter3=0
  Counter4=0
  m=["_prg.o","_cfg.o"]
  for i in m:  
    match=re.search(r'[\w+](\w*)  .text\s+'+string+i,text)
    if match:
      res = int(match.group(1), 16)
      Counter1=Counter1+res
    match1=re.search(r'[\w+](\w*)  .rodata\s+'+string+i,text)
    if match1:
      res = int(match1.group(1), 16)
      Counter2=Counter2+res
    match2=re.search(r'[\w+](\w*)  .data\s+'+string+i,text)
    if match2:
      res = int(match2.group(1), 16)
      Counter3=Counter3+res
    match3=re.search(r'[\w+](\w*)  .bss\s+'+string+i,text)
    if match3:
      res = int(match3.group(1), 16)
      Counter4=Counter4+res
  print('Size of .text     section in '+string+' component is = '+str(Counter1)+' Bytes')
  print('Size of .rodata   section in '+string+' component is = '+str(Counter2)+' Bytes')
  print('Size of .data     section in '+string+' component is = '+str(Counter3)+' Bytes')
  print('Size of .bss      section in '+string+' component is = '+str(Counter4)+' Bytes')
  
  print('Size of ROM in '+string+' component is = '+str(Counter1+Counter2)+' Bytes')
  print('Size of ROM in '+string+' component is = '+str(Counter3+Counter4)+' Bytes')
  
  f=open(string+'MY_info.txt','w')
  f.write("***** "+string+" component Info *****\n")
  f.write('Size of .text     section in '+string+' component is = '+str(Counter1)+' Bytes\n')
  f.write('Size of .rodata   section in '+string+' component is = '+str(Counter2)+' Bytes\n')
  f.write('Size of .data     section in '+string+' component is = '+str(Counter3)+' Bytes\n')
  f.write('Size of .bss      section in '+string+' component is = '+str(Counter4)+' Bytes\n')
  
  f.write('Size of ROM in '+string+' component is = '+str(Counter1+Counter2)+' Bytes\n')
  f.write('Size of RAM in '+string+' component is = '+str(Counter3+Counter4)+' Bytes\n')
  
  
def main():
  if len(sys.argv) == 2:
    print(sys.argv[1])
    fun(sys.argv[1])
  else:
    print("Please enter only one component")
main()