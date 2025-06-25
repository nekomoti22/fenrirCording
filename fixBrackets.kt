/*小括弧'()'と中括弧'{}'と大括弧'[]'のみで構成された文字列 s が与えられた時、s が下記のルールに従っているか判定するプログラムを作成せよ。*/
/*ルール1:開き括弧'({['は、同じ種類の閉じ括弧')}]'で閉じること*/
/*ルール2:括弧を開いた順に括弧を閉じること*/

fun isValid(s: String): Boolean {
    val decomp = s.chunked(1) //受け取った文を1文字ずづに分ける
    val bra = ArrayDeque<String>() //Stack
    val match = mapOf(")" to "(", "]" to "[", "}" to "{")

    for(i in decomp){
        if((i == "(")or(i == "[")or(i == "{")){
            bra.addLast(i)
        }else{
            if(bra.firstOrNull() == null){
                return false
            }
            if (match[i] == bra.last()){
                bra.removeLast()
            }else{
                return false               
            }
        }
    } 
    if(bra.firstOrNull() == null){
        return true
    }else{
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

    s = ")"
    println(isValid(s))  // false
}
