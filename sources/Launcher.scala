 // See LICENSE.txt for license details.
package RCA
import chisel3._
import chisel3.iotesters.{Driver, TesterOptionsManager}
import utils.TutorialRunner

object Launcher {
  val apr_num = APR_NUM_SUB
  val test = "TYPE_SUB"
  val tests = Map(
    "RCA" -> { (manager: TesterOptionsManager) =>
      Driver.execute(() => new RcaAdder(8), manager) {
        (c) => new AdderTester(c,256)
      }
    },
    "RCA_A" -> { (manager: TesterOptionsManager) =>
      Driver.execute(() => new RcaAdder_A_1(8,apr_num,test), manager) {
        println("Actual Test",apr_num," ",test)
        (c) => new AdderTester_A_1(c,256)
      }
    }
  )

  def main(args: Array[String]): Unit = {
    TutorialRunner("RCA", tests, args)
  }
}

