from langgraph.graph import StateGraph
from app.langgraph.state import ResumeState

from app.langgraph.nodes.extract_skills_node import (
    extract_skills_node
)

from app.langgraph.nodes.normalize_skills_node import (
    normalize_skills_node
)

from app.langgraph.nodes.expand_skills_node import (
    expand_skills_node
)

from app.langgraph.nodes.semantic_match_node import (
    semantic_match_node
)

from app.langgraph.nodes.scoring_node import (
    scoring_node
)

from app.langgraph.nodes.explanation_node import (
    explanation_node
)

workflow = StateGraph(ResumeState)

workflow.add_node(
    "extract",
    extract_skills_node
)

workflow.add_node(
    "normalize",
    normalize_skills_node
)

workflow.add_node(
    "expand",
    expand_skills_node
)

workflow.add_node(
    "semantic_match",
    semantic_match_node
)

workflow.add_node(
    "score",
    scoring_node
)

workflow.add_node(
    "explanation",
    explanation_node
)

workflow.set_entry_point("extract")

workflow.add_edge("extract", "normalize")

workflow.add_edge("normalize", "expand")

workflow.add_edge("expand", "semantic_match")

workflow.add_edge("semantic_match", "score")

workflow.add_edge("score", "explanation")

app_workflow = workflow.compile()