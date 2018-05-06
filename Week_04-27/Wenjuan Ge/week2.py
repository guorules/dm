from scipy import spatial

# check document1
f = open('document1.txt', 'r')
line = f.read().lower()
set1 = [line.count('messi'), line.count('barcelona'),
                    line.count('suarez'), line.count('title'), line.count('soccer')]
print1 = 'Check frequency from document1:'
messi = ' Messi:', line.count('messi')
barcelona = ' Barcelona:', line.count('barcelona')
suarez = ' Suarez:', line.count('suarez')
title = ' Title:', line.count('title')
soccer = 'Soccer:', line.count('soccer')

# check document2
f2 = open('document2.txt', 'r')
line2 = f2.read().lower()
set2 = [line2.count('messi'), line2.count('barcelona'),
                    line2.count('suarez'), line2.count('title'), line2.count('soccer')]
print2 = 'Check frequency from document2:'
messi2 = ' Messi:', line2.count('messi')
barcelona2 = ' Barcelona:', line2.count('barcelona')
suarez2 = ' Suarez:', line2.count('suarez')
title2 = ' Title:', line2.count('title')
soccer2 = ' Soccer:', line2.count('soccer')

# fine Cosine Similarity
result = 1 - spatial.distance.cosine(set1, set2)
results = 'Cosine Similarity is', result

# write the final result (cosine similarity) in a file called output.txt.
with open('Output.txt', 'w') as output:

    newline = '{:5}\n  {:5}\n  {:5}\n  {:5}\n  {:5}\n  {:5}\n'.format(print1, messi, barcelona, suarez, title, soccer)
    newline2 = '\n{:5}\n  {:5}\n  {:5}\n  {:5}\n  {:5}\n  {:5}\n'.format(print2, messi2, barcelona2, suarez2, title2, soccer2)
    newline3 = '\n{:5}\n'.format(results)
    output.write(newline)
    output.write(newline2)
    output.write(newline3)
