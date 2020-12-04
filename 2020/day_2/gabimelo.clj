; shared

(defn str-split [input-str] (clojure.string/split input-str #" "))

(def input-lines (map str-split (clojure.string/split-lines (slurp "gabimelo.txt"))))

(defn specified-letter [input-line] (nth (nth input-line 1) 0 ))

(defn policy-number [input-line number-index] 
	(Integer/parseInt 
		(nth 
			(clojure.string/split 
			 ( nth input-line 0 ) #"-") 
			 number-index
			)
	)
)

; part 1

(defn letter-frequency [input-line]
	(get 
	 (frequencies 
	 	 (nth input-line 2)
	 ) 
  (specified-letter input-line)
  -1 ; will be -1 if not found
 )
)

(defn check-valid [input-line]
	(if 
		(and
			(>= 
			 (letter-frequency input-line)
				(policy-number input-line 0)
			)
			(<= 
				(letter-frequency input-line)
				(policy-number input-line 1)
			)
	) 
	true 
	)
)

(count (filter identity (map check-valid input-lines)))

; part 2

(defn position-check [input-line policy-index]
	(= 
	 (nth
	 	(nth input-line 2) 
			(- (policy-number input-line policy-index) 1)
		)
	 (specified-letter input-line)
	)
)

(defn check-valid [input-line]
	(if 
		(and 
			(or
 				(position-check input-line 0)
 				(position-check input-line 1)
 		)
 		(not 
 			(and
	 				(position-check input-line 0)
	 				(position-check input-line 1)
	 		)
	 	)
	) 
	true 
	)
)

(count (filter identity (map check-valid input-lines)))
