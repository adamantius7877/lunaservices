from Models.Neo4j import LunaBlueprint, LunaKeyword

class CommandFactory(object):

    def GetBlueprints(self, tokens, tags):
        # Match the blueprint directive with the token
        # Filter the relationship based on the tag

        # Get the keywords associated with all tokens
        keyword = LunaKeyword()
        keywords = keyword.GetAny(tokens)#.nodes.filter(name__in=tokens)

        # Filter the keywords based on their directives and the tags they contain
        blueprints = []#keywords.Directives.match(Tags__in=tags)

        return blueprints

    def GetPossibleCommands(self, processedSentence):
        # First check if the sentence is valid
        if not self.ValidateSentence(processedSentence):
            return

        # Get a list of the tags and tokens
        tokens = []
        tags = []
        for tagPair in processedSentence.OrderedTags:
            tags.append(tagPair[0])
            tokens.append(tagPair[1])

        # Get a list of possible blueprints this command is for based on directive
        blueprints = self.GetBlueprints(tokens, tags)

    def ValidateSentence(self, processedSentence):
        return processedSentence is not None

