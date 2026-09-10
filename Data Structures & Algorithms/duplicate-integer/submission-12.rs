impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mut set : HashSet<i32>= HashSet::new();
        for i in &nums{
            if set.contains(i) {
                return true
            }
            // println!("{i}");
            set.insert(*i);
        }
    return false;
    }
}
