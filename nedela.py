def nedela(diena):
  if diena<1 or diena >7:
    print("Nav diena")
  elif diena == 1:
    print("Pirmdiena")
  elif diena == 2:
    print("Otrdiena")
  elif diena == 3:
    print("Trešdiena")
  elif diena == 4:
    print("Ceturtdiena")
  elif diena == 5:
    print("Piektdiena")
  elif diena == 6:
    print("Sestdiena")
  else:
    print("Svētdiena")
  return(diena)