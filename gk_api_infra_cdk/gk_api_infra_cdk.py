from aws_cdk import (
  Stack,
  RemovalPolicy,
  aws_s3 as s3,
  aws_dynamodb as db,
  aws_lambda as _lambda
)

from constructs import Construct

class GkCdkStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    swetha_bucket = s3.Bucket(self, "SwethaBucket",
      versioned=True,
      removal_policy=RemovalPolicy.DESTROY,
      auto_delete_objects=True
    )

    user_table = db.TableV2(self, "UsersTable",
      table_name="users_table",
      partition_key=db.Attribute(name="id", type=db.AttributeType.STRING),
      removal_policy=RemovalPolicy.DESTROY
    )

    # users_function_props = _lambda.FunctionProps(self, "UsersFunctionProps",
    #   runtime=_lambda.Runtime.PYTHON_3_10,
    #   handler="app.lambda_handler",
    #   code=_lambda.Code.from_asset("functions/users_function"),
    #   environment={
    #     "GK_USER_TABLE_NAME": user_table.table_name
    #   }
    # )

    users_function = _lambda.Function(
      self,
      "UsersFunction",
      runtime=_lambda.Runtime.PYTHON_3_11,
      handler="app.lambda_handler",
      code=_lambda.Code.from_asset("functions/users_function"),
      environment={
        "GK_USER_TABLE_NAME": user_table.table_name
      }
    )