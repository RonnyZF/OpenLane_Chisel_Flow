// See LICENSE.txt for license details.
package RCA
import chisel3._
import chisel3.iotesters.{Driver, TesterOptionsManager}
import utils.TutorialRunner

object Launcher {
  val apr_num = APR_NUM_SUB
  val pri_type = PRI_TYPE_SUB
  val sub_type = SUB_TYPE_SUB
  val tests = Map(
    "RCA" -> { (manager: TesterOptionsManager) =>
      Driver.execute(() => new RcaAdder(8), manager) {
        (c) => new AdderTester(c,256)
      }
    },
    "RCA_A" -> { (manager: TesterOptionsManager) =>
      Driver.execute(() => new RcaAdder_A_1(8,apr_num,pri_type,sub_type), manager) {
        (c) => new AdderTester_A_1(c,256)
      }
    }
  )

  def main(args: Array[String]): Unit = {
    println (args)
    TutorialRunner("RCA", tests, args)
  }
}
