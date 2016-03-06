class Executor
  def initialize(description, tests)
    @description = description
    @tests = tests
    @success_count = 0
    @failure_count = 0
  end
  def execute
    puts "#{@description}"
    @tests.each_pair do |name, block|
      print " - #{name}"
      result = self.instance_eval(&block)
      result ? @success_count += 1 : @failure_count += 1
      puts result ? " SUCCESS" : " FAILURE"
    end
    summary
  end
  def summary
    puts "\n#{@tests.keys.size} tests, #{@success_count} success, #{@failure_count} failure"
  end
end