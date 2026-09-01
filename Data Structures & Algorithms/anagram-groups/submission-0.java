class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<>();
        HashMap<HashMap, Integer> sublists = new HashMap<>();
        for (String s: strs) {
            HashMap<Character, Integer> anagrams = new HashMap<>();
            for (char c: s.toCharArray()) {
                anagrams.put(c, anagrams.getOrDefault(c, 0) + 1);
            }
            //System.out.println(s + " " + anagrams);
            if (sublists.containsKey(anagrams)) {
               // System.out.println("Found anagram for " + s);
                //System.out.println("Anagram " + output.get(sublists.get(anagram)).get(0) + " at index " + sublists.get(anagram));
                output.get(sublists.get(anagrams)).add(s);
            } else {
                sublists.put(anagrams, output.size());
                output.add(new ArrayList<>(Arrays.asList(s)));
            }
        }
        return output;
    }
}
