gawk -F, 'NR > 1 && $3 == 2 && $NF ~ "S" {print $0}' titanic.csv |
gawk -F, '{gsub(/female/, "F"); print $0}' | gawk -F, '{gsub(/male/, "M"); print $0}' |
gawk -F, '$7 > 0 {count += 1 && sum += $7} END {average = sum/count} {print $0} END {print "Average Age:" average}'
