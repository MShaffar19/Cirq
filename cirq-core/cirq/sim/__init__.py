# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Classes for circuit simulators and base implementations of these classes."""
from typing import Tuple, Dict

from cirq.sim.act_on_args import ActOnArgs

from cirq.sim.act_on_args_container import ActOnArgsContainer

from cirq.sim.act_on_density_matrix_args import ActOnDensityMatrixArgs

from cirq.sim.act_on_state_vector_args import ActOnStateVectorArgs

from cirq.sim.density_matrix_utils import measure_density_matrix, sample_density_matrix

from cirq.sim.density_matrix_simulator import (
    DensityMatrixSimulator,
    DensityMatrixSimulatorState,
    DensityMatrixStepResult,
    DensityMatrixTrialResult,
)

from cirq.sim.operation_target import OperationTarget

from cirq.sim.mux import (
    CIRCUIT_LIKE,
    final_density_matrix,
    final_state_vector,
    sample,
    sample_sweep,
)

from cirq.sim.simulator import (
    SimulatesAmplitudes,
    SimulatesExpectationValues,
    SimulatesFinalState,
    SimulatesIntermediateState,
    SimulatesSamples,
    SimulationTrialResult,
    StepResult,
)

from cirq.sim.simulator_base import SimulationTrialResultBase, SimulatorBase, StepResultBase

from cirq.sim.sparse_simulator import Simulator, SparseSimulatorStep

from cirq.sim.state_vector_simulator import (
    SimulatesIntermediateStateVector,
    StateVectorSimulatorState,
    StateVectorStepResult,
    StateVectorTrialResult,
)

from cirq.sim.state_vector import measure_state_vector, sample_state_vector, StateVectorMixin

from cirq.sim.clifford import (
    ActOnCliffordTableauArgs,
    ActOnStabilizerCHFormArgs,
    ActOnStabilizerArgs,
    StabilizerSampler,
    StabilizerStateChForm,
    CliffordSimulator,
    CliffordState,
    CliffordTrialResult,
    CliffordSimulatorStepResult,
)
