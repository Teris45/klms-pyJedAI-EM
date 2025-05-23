package enums;

import datareader.*;
import workflowManager.CommandLineInterface;

import java.util.HashSet;

import com.google.gson.*;

import static workflowManager.CommandLineInterfaceUtils.*;

public enum DataType {
    CSV,
    TSV,
    GeoJSON,
    JSONRDF,
    RDF;

    public static AbstractReader getReader(DataType dataType, String filepath) {

        int geoIndex;
        int attributeFirstRow;
        switch (dataType) {

            case CSV:
                geoIndex = readInt("Please provide the index of the geometry:");
                attributeFirstRow = readInt("Please denote if the input dataset contains attributes at the first row:", YES_OR_NO);
                return new GeometryCSVReader(attributeFirstRow == 1, ',', geoIndex, new int[]{}, filepath);

            case TSV:
                geoIndex = readInt("Please provide the index of the geometry:");
                attributeFirstRow = readInt("Please denote if the input dataset contains attributes at the first row:", YES_OR_NO);
                return new GeometryCSVReader(attributeFirstRow == 1, '\t', geoIndex, new int[]{}, filepath);

            case RDF:
                return new GeometryRDFReader(filepath, new HashSet<>());

            case JSONRDF:
                String prefix = readPath("Please provide the prefix of the RDF triples:");
                return new GeometryJSONRDFReader(filepath, prefix, new HashSet<>());

            case GeoJSON:
                return new GeometryGeoJSONReader(filepath);
        }

        return null;
    }


    public static AbstractReader getReader(DataType dataType, String filepath, JsonObject input_json) {
        int geoIndex;
        boolean attributeFirstRow;

        switch (dataType) {
            case CSV:
                geoIndex = input_json.get("geo_index").getAsInt();
                attributeFirstRow = input_json.get("attributes_first_row").getAsBoolean();
                return new GeometryCSVReader(attributeFirstRow, ',', geoIndex, new int[]{}, filepath);
            case TSV:
                geoIndex = input_json.get("geo_index").getAsInt();
                attributeFirstRow = input_json.get("attributes_first_row").getAsBoolean();
                return new GeometryCSVReader(attributeFirstRow, '\t', geoIndex, new int[]{}, filepath);
            case RDF:
                return new GeometryRDFReader(filepath, new HashSet<>());
            case JSONRDF:
                String prefix = input_json.get("prefix_RDF").getAsString();
                return new GeometryJSONRDFReader(filepath, prefix, new HashSet<>());
            case GeoJSON:
                return new GeometryGeoJSONReader(filepath);
        }
        

        return null;
    }
}
