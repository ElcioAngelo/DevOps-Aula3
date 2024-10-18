import { Box, Button, ButtonGroup, Card, CardBody, CardFooter, Divider, Heading, Image, Stack, Text } from "@chakra-ui/react";
import axios from "axios";
import { useEffect, useState } from "react";


const RecipeCard = ({ category, description, price, title }) => {
    return (
        <Card maxW="80">
            <CardBody>
                <Stack mt='6' spacing='3'>
                    <Heading size='md'>{title}</Heading>
                    <Text>
                        {description}
                    </Text>
                    <Text color='blue.600' fontSize='2xl'>
                        R$ {price}
                    </Text>
                </Stack>
            </CardBody>
            <Divider />
            <CardFooter>
                <Text>{category}</Text>
            </CardFooter>
        </Card>
    )

}



const Receitas = () => {

    const [receitas, setReceitas] = useState([])

    const getReceitas = async () => {
        try {
            const receitas = await axios.get("http://127.0.0.1:5000")
            setReceitas(receitas.data)
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        getReceitas()
    }, [])

    return (
        <Box
            backgroundColor={"black"}
            width={"100%"}
            height={"auto"}
            display={"flex"}
            paddingBlock={50}
            paddingInline={10}
            flexWrap={"wrap"}
            gap={10}
            justifyContent={"center"}
        >
            {receitas.map((item, index) => {
                return (
                    <RecipeCard
                        category={item.category}
                        price={item.price}
                        title={item.title}
                        description={item.description}
                    />
                )
            })}

        </Box>
    );
}

export default Receitas;