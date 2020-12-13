class Utils {
    companion object {
        fun String.splitAtIndex(index: Int) = take(index) to substring(index)
    }
}