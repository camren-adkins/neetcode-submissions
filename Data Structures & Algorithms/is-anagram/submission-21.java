class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            if(sMap.get(c) == null)
            sMap.put(c, 0);
            sMap.put(c, (sMap.get(c) + 1));
        }
        for (char c : t.toCharArray()) {
            if(tMap.get(c) == null)
            tMap.put(c, 0);
            tMap.put(c, (tMap.get(c) + 1));
        }
        /*
        if (sMap.size() > tMap.size()) {
            System.out.print("first triggered ");
            for (char c : sMap.keySet()) {
            if (sMap.get(c) != tMap.get(c))
            return false;
        }
        }
        else {
            System.out.print("second triggered ");
            for (char c : tMap.keySet()) {
            System.out.println(tMap.get(c) + " " + sMap.get(c));
            if((tMap.get(c) != null) && (sMap.get(c) != null))
            System.out.println((int)(tMap.get(c)) != (int)(sMap.get(c)));
            System.out.println(tMap.get(c) != sMap.get(c));
            System.out.println(((tMap.get(c) == null) ^ (sMap.get(c) == null)) || (tMap.get(c) != sMap.get(c)));
            if ((sMap.get(c) == null) || ((int)tMap.get(c) != (int)sMap.get(c))) {
                System.out.print(tMap.get(c) + " " + sMap.get(c));
            return false;
            }
        }
        
        }
        */
        return sMap.equals(tMap);
    }
}
