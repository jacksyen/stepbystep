class Account
  attr_accessor :balance
  def initialize(balance)
    @balance = balance
  end

  def debit(amt)
    if @balance <amt
      fail "Insufficient funds"
    else
      @balance -=amt
    end
  end
end

account = Account.new(456)
account.debit(400)

puts account.balance