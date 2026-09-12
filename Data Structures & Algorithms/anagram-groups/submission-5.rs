impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        use std::collections::HashMap;
        let mut sort_dict: HashMap<String, Vec<String>> = HashMap::new();
        for word in &strs{
            let mut chars:Vec<char>= word.chars().collect();
            chars.sort();
            let sorted_string: String = chars.into_iter().collect();

           
            sort_dict.entry(sorted_string).or_default().push(word.clone())
        }
        
        sort_dict.into_values().collect()


    }
}
