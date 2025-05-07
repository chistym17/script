URL="https://www.amfiindia.com/spages/NAVAll.txt"

OUTPUT="schemes.tsv"

curl -s "$URL" | awk -F ';' 'NF >= 5 && $4 != "Scheme Name" { print $4 "\t" $5 }' > "$OUTPUT"

echo "Extracted data saved to $OUTPUT"
