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
# 
###############################################################################
# Module:  factory
# Purpose: Build concrete instances of specific appliers
#
# Notes:
#
###############################################################################

import data_pipeline.constants.const as const
from data_pipeline.db.exceptions import UnsupportedDbTypeError


def build(mode, source_processor, db, argv, audit_factory):
    """Return the specific type of applier object given the dbtype_name"""
    if db.dbtype == const.POSTGRES:
        if mode == const.INITSYNCAPPLY:
            from data_pipeline.applier.postgres_initsync_applier import (
                PostgresInitSyncApplier
            )
            return PostgresInitSyncApplier(source_processor, db,
                                           argv, audit_factory)
        else:
            from data_pipeline.applier.postgres_cdc_applier import (
                PostgresCdcApplier
            )
            return PostgresCdcApplier(source_processor, db,
                                      argv, audit_factory)
    elif db.dbtype == const.GREENPLUM:
        from data_pipeline.applier.greenplum_cdc_applier import (
            GreenplumCdcApplier
        )
        return GreenplumCdcApplier(source_processor, db,
                                   argv, audit_factory)
    else:
        raise UnsupportedDbTypeError(db.dbtype)
