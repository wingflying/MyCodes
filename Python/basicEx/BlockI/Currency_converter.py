"""
    作者：李向荣
    功能：汇率变换
    功能+1：新增输入货币判断，自动按人民币或美元转换成对应货币，否则退出；
    功能+2：增加循环判断，持续运行、直到输入；
    功能+3：将变换功能封装到函数里；
    功能+4：程序结构化封装及简单函数Lamda；
    日期：2019/8/12
"""

def main():
    """
        主函数
    """

    # 汇率比值
    USD_vs_RMB = 6.77

    # 输入货币数值
    currency_str_value = input('请输入货币数值：')
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_vs_RMB

    elif unit == 'USD':
        exchange_rate = USD_vs_RMB

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        # 使用lambda定义函数
        convert_currency2 = lambda x: x * exchange_rate

        # # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)

        # 调用lambda函数
        out_money = convert_currency2(in_money)
        print('转换后的金额：', out_money)
    else:
        print('不支持该种货币！')

if __name__ == '__main__':
    main()