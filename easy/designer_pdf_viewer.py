# designer pdf viewer

def designerPdfViewer(h, word):
  max_height = 0
  for char in word:
    code = ord(char)
    curr_height = h[code - 97]
    if curr_height > max_height:
      max_height = curr_height
  return len(word) * max_height

h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7"
h = list(map(int, h.split()))
word = "zaba"

print(designerPdfViewer(h, word))