(def docs (clojure.string/split (slurp "gabimelo.txt") #"\n\n"))

(def required-keys (set '("byr" "iyr" "eyr" "hgt" "hcl" "ecl" "pid")))

(defn get-doc-pieces [doc] (clojure.string/split doc #"\s"))

(defn get-doc-hash [doc] 
  (into {} (map #(apply hash-map (clojure.string/split % #":")) (get-doc-pieces doc))))

; part 1

(defn get-missing-keys [required-keys doc] 
  (clojure.set/difference required-keys (set (keys (get-doc-hash doc)))))

(defn keys-match? [required-keys doc]
  (= 0 (count (get-missing-keys required-keys doc))))

(defn valid-doc? [required-keys doc] 
  (keys-match? required-keys doc))

(count 
  (filter identity 
    (map 
      (partial valid-doc? required-keys) docs)))

; part 2

(def validation-rules {
  "byr" #"^(19[2-9][0-9]|200[0-2])$"
  "iyr" #"^(20(1[0-9]|20))$"
  "eyr"  #"^(20(2[0-9]|30))$"
  "hgt" #"^((1(([5-8][0-9])|(9[0-3]))cm)|(((59)|(6[0-9])|(7[0-6]))in))$"
  "hcl" #"^(\#[0-9|a-f]{6})$"
  "ecl" #"^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))$"
  "pid" #"^([0-9]{9})$"})

(defn values-valid? [validation-rules doc] 
  (every?
  identity 
  (for [rule validation-rules] 
      (if (re-matches (nth rule 1) ((get-doc-hash doc) (nth rule 0))) true false))))

(defn valid-doc? [required-keys validation-rules doc] 
  (and (keys-match? required-keys doc) (values-valid? validation-rules doc)))

(count 
  (filter identity 
    (map 
      (partial valid-doc? required-keys validation-rules) docs)))
