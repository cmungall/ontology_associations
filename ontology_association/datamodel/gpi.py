# Auto generated from gpi.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 10:55
# Schema: gpi
#
# id: https://w3id.org/ontology_association/gpi
# description: Various association data models
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from . association import AbstractThingId, BiologicalEntity, Curie, Document, NameType, PropertyValuePair, SymbolType, TaxonId
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ONTOLOGY_ASSOCIATION = CurieNamespace('ontology_association', 'https://w3id.org/ontology_association/')
DEFAULT_ = ONTOLOGY_ASSOCIATION


# Types

# Class references
class GpiEntityDbObjectRef(AbstractThingId):
    pass


@dataclass
class GpiEntity(BiologicalEntity):
    """
    An entity that can be annotated using GO. May be a gene, gene product, or complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpiEntity
    class_class_curie: ClassVar[str] = "ontology_association:GpiEntity"
    class_name: ClassVar[str] = "gpi entity"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpiEntity

    db_object_ref: Union[str, GpiEntityDbObjectRef] = None
    db_object_symbol: Union[str, SymbolType] = None
    db_object_taxon: Union[str, TaxonId] = None
    db_object_name: Optional[Union[str, NameType]] = None
    db_object_synonyms: Optional[Union[Union[str, NameType], List[Union[str, NameType]]]] = empty_list()
    db_object_type: Optional[str] = None
    encoded_by: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    parent_protein: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    protein_containing_complex_members: Optional[Union[Union[str, AbstractThingId], List[Union[str, AbstractThingId]]]] = empty_list()
    db_xrefs: Optional[Union[Union[str, Curie], List[Union[str, Curie]]]] = empty_list()
    gene_product_properties: Optional[Union[Union[dict, PropertyValuePair], List[Union[dict, PropertyValuePair]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.db_object_ref is None:
            raise ValueError("db_object_ref must be supplied")
        if not isinstance(self.db_object_ref, GpiEntityDbObjectRef):
            self.db_object_ref = GpiEntityDbObjectRef(self.db_object_ref)

        if self.db_object_symbol is None:
            raise ValueError("db_object_symbol must be supplied")
        if not isinstance(self.db_object_symbol, SymbolType):
            self.db_object_symbol = SymbolType(self.db_object_symbol)

        if self.db_object_taxon is None:
            raise ValueError("db_object_taxon must be supplied")
        if not isinstance(self.db_object_taxon, TaxonId):
            self.db_object_taxon = TaxonId(self.db_object_taxon)

        if self.db_object_name is not None and not isinstance(self.db_object_name, NameType):
            self.db_object_name = NameType(self.db_object_name)

        if self.db_object_synonyms is None:
            self.db_object_synonyms = []
        if not isinstance(self.db_object_synonyms, list):
            self.db_object_synonyms = [self.db_object_synonyms]
        self.db_object_synonyms = [v if isinstance(v, NameType) else NameType(v) for v in self.db_object_synonyms]

        if self.db_object_type is not None and not isinstance(self.db_object_type, str):
            self.db_object_type = str(self.db_object_type)

        if self.encoded_by is None:
            self.encoded_by = []
        if not isinstance(self.encoded_by, list):
            self.encoded_by = [self.encoded_by]
        self.encoded_by = [v if isinstance(v, AbstractThingId) else AbstractThingId(v) for v in self.encoded_by]

        if self.parent_protein is None:
            self.parent_protein = []
        if not isinstance(self.parent_protein, list):
            self.parent_protein = [self.parent_protein]
        self.parent_protein = [v if isinstance(v, AbstractThingId) else AbstractThingId(v) for v in self.parent_protein]

        if self.protein_containing_complex_members is None:
            self.protein_containing_complex_members = []
        if not isinstance(self.protein_containing_complex_members, list):
            self.protein_containing_complex_members = [self.protein_containing_complex_members]
        self.protein_containing_complex_members = [v if isinstance(v, AbstractThingId) else AbstractThingId(v) for v in self.protein_containing_complex_members]

        if self.db_xrefs is None:
            self.db_xrefs = []
        if not isinstance(self.db_xrefs, list):
            self.db_xrefs = [self.db_xrefs]
        self.db_xrefs = [v if isinstance(v, Curie) else Curie(v) for v in self.db_xrefs]

        if self.gene_product_properties is None:
            self.gene_product_properties = []
        if not isinstance(self.gene_product_properties, list):
            self.gene_product_properties = [self.gene_product_properties]
        self.gene_product_properties = [v if isinstance(v, PropertyValuePair) else PropertyValuePair(**v) for v in self.gene_product_properties]

        super().__post_init__(**kwargs)


@dataclass
class GpiDocument(Document):
    """
    A collection of gpi entities plus associated metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpiDocument
    class_class_curie: ClassVar[str] = "ontology_association:GpiDocument"
    class_name: ClassVar[str] = "gpi document"
    class_model_uri: ClassVar[URIRef] = ONTOLOGY_ASSOCIATION.GpiDocument

    entities: Optional[Union[Union[str, GpiEntityDbObjectRef], List[Union[str, GpiEntityDbObjectRef]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.entities is None:
            self.entities = []
        if not isinstance(self.entities, list):
            self.entities = [self.entities]
        self.entities = [v if isinstance(v, GpiEntityDbObjectRef) else GpiEntityDbObjectRef(v) for v in self.entities]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.gpiDocument__entities = Slot(uri=ONTOLOGY_ASSOCIATION.entities, name="gpiDocument__entities", curie=ONTOLOGY_ASSOCIATION.curie('entities'),
                   model_uri=ONTOLOGY_ASSOCIATION.gpiDocument__entities, domain=None, range=Optional[Union[Union[str, GpiEntityDbObjectRef], List[Union[str, GpiEntityDbObjectRef]]]])

slots.gpi_entity_db_object_ref = Slot(uri=ONTOLOGY_ASSOCIATION.db_object_ref, name="gpi entity_db object ref", curie=ONTOLOGY_ASSOCIATION.curie('db_object_ref'),
                   model_uri=ONTOLOGY_ASSOCIATION.gpi_entity_db_object_ref, domain=GpiEntity, range=Union[str, GpiEntityDbObjectRef])
