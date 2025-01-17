# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from marshmallow import Schema, fields


class VariableSchema(Schema):
    """Variable Schema"""

    key = fields.String(required=True)
    value = fields.String(attribute="val", required=True)
    description = fields.String(attribute="description", required=True)

class VariableCollectionSchema(Schema):
    """Variable Collection Schema"""

    variables = fields.List(fields.Nested(VariableSchema))
    total_entries = fields.Int()


variable_schema = VariableSchema()
variable_collection_schema = VariableCollectionSchema()
