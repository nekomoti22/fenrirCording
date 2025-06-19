fun isValid(s: String): Boolean {
    val decomp = s.chunked(1)
    println(decomp) 
    var parenFlag = false
    var squaFlag = false
    var curlyFlag = false
    for (i in decomp){
        when(i) {
            // 括弧はじめ
            "(" -> if (parenFlag == true){
                return false
            } else{
                parenFlag = true
            }
            "[" -> if (squaFlag == true){
                return false
            } else{
                squaFlag = true
            }
            "{" -> if (curlyFlag == true){
                return false
            } else{
                curlyFlag = true
            }
            // 括弧閉じる
            ")" -> if (parenFlag == true){
                parenFlag = false
            } else {
                return false
            }
            "]" -> if (parenFlag == true){
                parenFlag = false
            } else {
                return false
            }
            "}" -> if (parenFlag == true){
                parenFlag = false
            } else {
                return false
            }
        }
    }
    // 最後にすべての括弧が開いたままでなければTrue
    if (parenFlag == false && squaFlag == false && curlyFlag == false) {
        return true
    } else {
        return false
    }
}

fun main(){
    var s = "()"
    println(isValid(s))  // true

    s = "({)}"
    println(isValid(s))  // false

    s = "("
    println(isValid(s))  // false
}
